echo "Configuring and building ORB_SLAM2 ..."
mkdir -p build
cd build
cmake .. -DCMAKE_BUILD_TYPE=Release
make -j

echo
echo "Test:"
cd ..
python3 test.py
