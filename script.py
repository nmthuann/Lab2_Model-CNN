import shutil
import os
import glob
import argparse
from numpy import random

# from path
from_base_path = ".\\out"
from_benign_path = from_base_path + "\\benign"
from_malware_path = from_base_path + "\\malware"
# chọn dst cho dataset
dest_base_path = ".\\dataset_1000"
dest_benign_1000_path = dest_base_path + "\\benign"
dest_malware_1000_path = dest_base_path + "\\malware"

test_base_path = ".\\test"
test_benign_path = test_base_path + "\\benign"
test_malware_path = test_base_path + "\\malware"

# thu thập tất cả các samples
benign_samples = glob.glob(".\\out\\benign\\*.png")
malware_samples = glob.glob(".\\out\\malware\\*.png")

maximum_dataset_size = min(len(benign_samples), len(malware_samples))


def rem_all_file(path):
    files = glob.glob(path + "\\*")
    for file in files:
        os.remove(file)


def get_random_malware_sample(size=1000, replace=False):
    return random.choice(malware_samples, size, replace)


def get_random_benign_sample(size=1000, replace=False):
    return random.choice(benign_samples, size, replace)


def get_random_test_sample(size=1000, replace=False, no_duplicate=False):
    non_dup_benign_samples = []
    non_dup_malware_samples = []

    if no_duplicate and os.path.exists('.\\dataset_1000\\benign') and os.path.exists('.\\dataset_1000\\malware'):
        print("[+] No duplicate enabled")

        duplicate_benign_samples = list(
            map(lambda name: name[len(dest_benign_1000_path) + 1:], glob.glob(dest_benign_1000_path + "\\*.png")))
        duplicate_malware_samples = list(
            map(lambda name: name[len(dest_malware_1000_path) + 1:], glob.glob(dest_malware_1000_path + "\\*.png")))
        # loại bỏ các sample trùng với dataset_1000
        non_dup_malware_samples = [mw_s for mw_s in malware_samples if
                                   mw_s[len(from_malware_path) + 1:] not in duplicate_malware_samples]
        print("[-] Got {} malware samples availables".format(len(non_dup_malware_samples)))
        non_dup_benign_samples = [bn_s for bn_s in benign_samples if
                                  bn_s[len(from_benign_path) + 1:] not in duplicate_benign_samples]
        print("[-] Got {} malware samples availables".format(len(non_dup_benign_samples)))

        maximum_test_dataset_size = min(len(non_dup_benign_samples), len(non_dup_malware_samples))

        if size > maximum_test_dataset_size:
            print("[!] Warning: dataset available less than requested size")
            size = maximum_test_dataset_size

    else:
        non_dup_benign_samples = benign_samples
        non_dup_malware_samples = malware_samples

    print("[+] Creating new test dataset with size {} per class".format(size))
    return (random.choice(non_dup_benign_samples, size, replace), random.choice(non_dup_malware_samples, size, replace))


def main():
    parser = argparse.ArgumentParser(description="Tools to generate dataset and tests sample")
    parser.add_argument('type', metavar='type', type=str,
                        help='generation type | all: genrate dataset and test | test: test only | train: train dataset only')
    parser.add_argument('--size', dest='size', type=int, default=1000, help='size per class')
    parser.add_argument('--no-duplicate', dest='no_dup', action='store_true',
                        help='set no duplicate on training set and test set')
    parser.add_argument('--clean', dest='type', type=str, help='clean all dataset')
    args = parser.parse_args()

    if args.size > maximum_dataset_size:
        print("[!] Warning: dataset available less than requested size")
        args.size = maximum_dataset_size

    if args.type == 'clean':
        if os.path.exists(dest_base_path):
            print("[+] Cleaning training dataset")
            shutil.rmtree(dest_base_path)
        if os.path.exists(test_base_path):
            print("[+] Cleaning test dataset")

    if args.type == 'train' or args.type == 'all':
        print("[+] Creating new train dataset with size {} per class".format(args.size))

        if not os.path.exists(dest_base_path):
            print("[!] Dataset not initialize")
            os.makedirs(dest_base_path)

        if not os.path.exists(dest_benign_1000_path):
            os.makedirs(dest_benign_1000_path)
        else:
            print("[!] Cleaning up old benign sample")
            rem_all_file(dest_benign_1000_path)

        if not os.path.exists(dest_malware_1000_path):
            os.makedirs(dest_malware_1000_path)
        else:
            print("[!] Cleaning up old malware sample")
            rem_all_file(dest_malware_1000_path)

        random_benign_sample = get_random_benign_sample(args.size)
        random_malware_sample = get_random_malware_sample(args.size)

        for i in random_benign_sample:
            shutil.copy(src=i, dst=dest_benign_1000_path)
        for i in random_malware_sample:
            shutil.copy(src=i, dst=dest_malware_1000_path)

    if args.type == 'test' or args.type == 'all':

        if not os.path.exists(test_base_path):
            os.makedirs(test_base_path)
        else:
            shutil.rmtree(test_base_path)

        os.makedirs(test_base_path + "\\benign")
        os.makedirs(test_base_path + "\\malware")

        random_malware_sample, random_benign_sample = get_random_test_sample(args.size, no_duplicate=args.no_dup)

        for i in random_malware_sample:
            shutil.copy(src=i, dst=test_benign_path)

        for i in random_benign_sample:
            shutil.copy(src=i, dst=test_malware_path)


if __name__ == "__main__":
    main()

    # python script.py - -size 100 - -no - duplicate all
    # configue CPU: python3 - c "import tensorflow as tf; print(tf.reduce_sum(tf.random.normal([1000, 1000])))"
    # configue GPU: python3 -c "import tensorflow as tf; print(tf.config.list_physical_devices('GPU'))"


