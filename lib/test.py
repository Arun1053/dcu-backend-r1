import sys
import os
 
current_dir = os.path.dirname(os.path.dirname(__file__))
dir2 = os.path.dirname(os.path.abspath(__file__))
# sys.path.append(r"D:\HGI\HGI-One yr\lib")
sys.path.append(current_dir)
print(current_dir, dir2)