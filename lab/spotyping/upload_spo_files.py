import os
import subprocess
import shutil


#######
# SCRATCH

# all_files = list(filter(lambda x: os.path.isfile(x), os.listdir()))


# for f in all_files:
#     subprocess.call(["rclone","copy", f , "onedrive-abhi:ena-genomes", "-vv"])

#rclone copy ERR036201_1.fastq.gz onedrive-abhi:ena-genomes -vv


#######



#rclone copy ERR036201_1.fastq.gz onedrive-abhi:ena-genomes -vv

def has_out_in_name(string):
    if (string.split(".")[-1] == "out"):
        #print("YES")
        return 1
    else:
        #print("NO")
        return 0



all_files = list(filter(lambda x: os.path.isfile(x), os.listdir()))
all_spo_files = list(filter(lambda x:has_out_in_name(x), all_files))
all_spo_files.remove("nohup.out")


for f in all_spo_files:
    subprocess.call(["rclone","copy", f , "onedrive-abhi:mozambique-genomes/lab/spotyping", "-vv"])
    shutil.move(f,"./uploaded/")
    #print(f)


