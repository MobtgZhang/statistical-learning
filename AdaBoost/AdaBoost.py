import os
import time
import urllib3
import random
import pandas as pd

def download(root_dir="./data"):
    if not os.path.exists(root_dir):
        os.mkdir(root_dir)
    files_list = ["winequality-red.csv","winequality-white.csv","winequality.names"]
    web_url = "https://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/"
    http = urllib3.PoolManager()
    for filename in files_list:
        response = http.request("GET",web_url+filename)
        save_filename = os.path.join(root_dir,filename)
        with open(save_filename,"wb") as wfp:
            wfp.write(response.data)
        response.release_conn()
def load_dataset(root_dir,train_per = 0.75):
    files_list = ["winequality-red.csv","winequality-white.csv"]
    data_list = []
    for filename in files_list:
        load_filename = os.path.join(root_dir,filename)
        dataset = pd.read_csv(load_filename,sep=";")
        data_list.append(dataset)
    dataset = pd.concat(data_list).to_numpy()
    random.shuffle(dataset)
    train_len = int(train_per*len(dataset))
    y_data = dataset[:,-1]
    x_data = dataset[:,:-1]
    x_train = x_data[:train_len]
    y_train = y_data[:train_len]
    x_test = x_data[train_len:]
    y_test = y_data[train_len:]
    return (x_train,y_train),(x_test,y_test)
def create_boost_tree(train_data,train_label,tree_num):
    pass
def main():
    start = time.time()
    root_dir = "./data"
    tree_num=40
    if not os.path.exists(root_dir):
        download(root_dir)
    print("The file is downloaded!")
    # load dataset
    train,test = load_dataset(root_dir)
    # create boost tree
    boost_tree = create_boost_tree(train[0],train[1],tree_num)    
    end = time.time()
    print("The time cost:%d"%(end-start))
if __name__ == "__main__":
    main()

