## run from root
VER=8.4.2
ITERATION=0
INSTALL_PATH=/opt/lmod/stable
MODULEFILES_PATH=/opt/uw/modulefiles

apt update
apt install -y git wget sed tclsh tcl-dev libreadline-dev

#** ensure packages
test -f lua-5.4.0.tar.gz || wget http://www.lua.org/ftp/lua-5.4.0.tar.gz
tar zxf lua-5.4.0.tar.gz -C ~
test -f luarocks-3.3.1.tar.gz || wget https://luarocks.org/releases/luarocks-3.3.1.tar.gz
tar zxpf luarocks-3.3.1.tar.gz -C ~

#** build lua
cd ~/lua-5.4.0
sed -i "s|/usr/local|$INSTALL_PATH/lua|" ./Makefile
sed -i "s|/usr/local/|$INSTALL_PATH/lua/|" ./src/luaconf.h
make linux
make install

#** build luarocks
cd ~/luarocks-3.3.1
./configure --prefix=$INSTALL_PATH/lua/  --with-lua=$INSTALL_PATH/lua
make install

#** build lmod lua requirements
$INSTALL_PATH/lua/bin/luarocks install luaposix
$INSTALL_PATH/lua/bin/luarocks install luajson
$INSTALL_PATH/lua/bin/luarocks install luafilesystem

#** build lmod
cd ~
git clone https://github.com/TACC/Lmod.git
cd ~/Lmod
git checkout $VER
export PATH=$INSTALL_PATH/lua/bin:$PATH

./configure --prefix=$INSTALL_PATH --with-siteControlPrefix=yes --with-useBuiltinPkgs=yes
make install

mkdir -p "$MODULEFILES_PATH"
mkdir -p "$MODULEFILES_PATH/init"
cat > $INSTALL_PATH/init/.modulespath <<EOF
$MODULEFILES_PATH
EOF
