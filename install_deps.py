"""
Dependency installer with fallback for PyArrow issues
Handles installation of PNEI Waddington Simulator dependencies
"""
import subprocess
import sys

def install_package(package):
    """Install package with error handling"""
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", package])
        return True
    except subprocess.CalledProcessError:
        return False

def main():
    print("=" * 60)
    print("PNEI Waddington Simulator - Dependency Installer")
    print("=" * 60)
    print(f"\nPython Version: {sys.version}")
    print(f"Python Executable: {sys.executable}\n")
    
    # Check Python version
    version_info = sys.version_info
    if version_info.major == 3 and version_info.minor >= 14:
        print("⚠️  WARNING: Python 3.14+ detected!")
        print("   Some packages may not have pre-built wheels available.")
        print("   Consider using Python 3.11 or 3.12 for better compatibility.\n")
    
    # Upgrade pip first
    print("Upgrading pip, setuptools, and wheel...")
    subprocess.check_call([sys.executable, "-m", "pip", "install", "--upgrade", "pip", "setuptools", "wheel"])
    print("✓ Package managers updated\n")
    
    # Core packages (required)
    core_packages = [
        ("numpy", "numpy>=1.24.0,<2.0.0"),
        ("plotly", "plotly>=5.17.0"),
        ("pandas", "pandas>=2.0.0")
    ]
    
    # Streamlit (may trigger PyArrow dependency)
    streamlit_package = "streamlit>=1.28.0"
    
    print("Installing core packages...")
    print("-" * 60)
    for name, pkg in core_packages:
        print(f"Installing {name}...", end=" ")
        if install_package(pkg):
            print("✓")
        else:
            print("✗ FAILED")
            print(f"\n❌ Error: Failed to install {name}")
            print(f"   Try manually: pip install {pkg}")
            return 1
    
    print("\nInstalling Streamlit...")
    print("-" * 60)
    
    # Try installing streamlit (may pull in pyarrow)
    print("Attempting Streamlit installation...", end=" ")
    if install_package(streamlit_package):
        print("✓")
    else:
        print("✗")
        print("\n⚠️  Streamlit installation failed. Trying fallback strategies...\n")
        
        # Strategy 1: Try with --only-binary for all packages
        print("Strategy 1: Installing with pre-built wheels only...", end=" ")
        try:
            subprocess.check_call([
                sys.executable, "-m", "pip", "install",
                "--only-binary", ":all:",
                streamlit_package
            ])
            print("✓")
        except subprocess.CalledProcessError:
            print("✗")
            
            # Strategy 2: Try older Streamlit version
            print("Strategy 2: Trying Streamlit 1.29.0...", end=" ")
            if install_package("streamlit==1.29.0"):
                print("✓ (using fallback version)")
            else:
                print("✗")
                
                print("\n❌ Installation Failed")
                print("\nRecommended solutions:")
                print("1. Use Python 3.11 or 3.12:")
                print("   py -3.12 -m venv .venv312")
                print("   .venv312\\Scripts\\activate")
                print("   python install_deps.py")
                print("\n2. Install via Conda:")
                print("   conda install -c conda-forge streamlit numpy plotly pandas")
                print("\n3. Try manual installation:")
                print("   pip install --only-binary :all: pyarrow")
                print("   pip install streamlit numpy plotly pandas")
                return 1
    
    print("\n" + "=" * 60)
    print("✅ Installation Complete!")
    print("=" * 60)
    print("\nTo run the simulator:")
    print("   streamlit run PNEI_Waddington_Simulator.py")
    print("\nThe application will open in your browser at:")
    print("   http://localhost:8501")
    print("\n")
    return 0

if __name__ == "__main__":
    sys.exit(main())
