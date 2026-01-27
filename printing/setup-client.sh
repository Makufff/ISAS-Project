#!/bin/bash

echo "🖨️  Setting up Print Client..."

# Install required Python packages
echo "📦 Installing required packages..."
pip3 install requests

# Get the script directory
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

# Create printfile command wrapper
echo "📝 Creating printfile command..."
cat > /usr/local/bin/printfile << 'EOF'
#!/bin/bash

if [ $# -ne 1 ]; then
    echo "Usage: printfile <filename>"
    exit 1
fi

# Get the directory where rpc-client.py is located
RPC_CLIENT_DIR="SCRIPT_DIR_PLACEHOLDER"

python3 "$RPC_CLIENT_DIR/rpc-client.py" "$1"
EOF

# Replace placeholder with actual script directory
sed -i "s|SCRIPT_DIR_PLACEHOLDER|$SCRIPT_DIR|g" /usr/local/bin/printfile

# Make printfile executable
chmod +x /usr/local/bin/printfile

echo "✅ Setup complete!"
echo ""
echo "You can now use: printfile <filename>"
echo ""
echo "Example:"
echo "  printfile solution.cpp"
echo ""
