from concurrent.futures.thread import _threads_queues
from doctest import DocTestParser
from multiprocessing.spawn import import_main_path
from operator import imod
import pandas as pd
import os
label_path = 'data/custom/labels.txt'
output_path = 'output/'

# 输入test结果
input_file = 'train_model14_entity0819.txt'
#所有类别的metric
output_file = 'output/result_model14_0819.txt'


# 输出文件名称
f_right = open(os.path.join(output_path, 'right_data_model14_0819.txt'), "w", encoding="utf-8")
f_wrong = open(os.path.join(output_path, 'wrong_data_model14_0819.txt'), "w", encoding="utf-8")

# test_path = 'data/custom/test_data.txt'
test_path = 'entity/train_data.txt'
# test_df = pd.read_csv(test_path,sep='\t',dtype=str,names=['query','label'])
test_df = pd.read_csv(test_path,sep='\t',dtype=str,names=['query','entity','label'])
test_list = test_df['query'].tolist()

labels_df = df = pd.read_csv(label_path,sep='\t',dtype=str)
df = pd.read_csv(input_file,sep='\t',dtype=str,names=['label','pred'])
pred_list = df['pred'].to_list()
true_list = df['label'].to_list()

num_classes = 54
labels = []
X = [0] * num_classes
Y = [0] * num_classes
Z = [0] * num_classes

def read_label(path):
	id2label = {}
	label2id = {}
	with open(path, "r", encoding="utf-8") as fin:
		for label_id,line in enumerate(fin):
			label = line.strip("\n")
			label2id[label] = str(label_id)
			id2label[str(label_id)] = label
	return label2id, id2label

def w_right_wrong(R,text,true):
    P_mul = []
    for i in range(len(R)):
        P_mul.append(id2label[str(R[i])])
    P_mul = ",".join(sorted(P_mul))
    T_mul = []
    for i in range(len(true)):
        T_mul.append(id2label[str(true[i])])
    T_mul = ",".join(sorted(T_mul))
    if P_mul == T_mul or P_mul in T_mul or (T_mul == '其他-未知意图-未知意图' and P_mul == ''):
        try:
            f_right.write(text + "\t" + str(P_mul) + "\t" + str(T_mul) + "\n")
        except Exception as e:
            print(text,P_mul,T_mul)
    else:
        #预测错误
        f_wrong.write(text + "\t" + P_mul + "\t" + T_mul + "\n")
        
label2id, id2label = read_label(label_path) 

for i in range(0, num_classes):
		labels.append(str(i))

for i,pred in enumerate(pred_list):
    true = true_list[i]
    for m in range(len(labels)):
        tmp = labels[m]
        if tmp == pred and tmp == true:
            # TP
            X[m] = X[m] + 1
        if tmp == pred:
            # TP+FP
            Y[m] = Y[m] + 1
        if tmp == true:
            # TP+FN
            Z[m] = Z[m] + 1
    # 写入 write 和wrong文件
    w_right_wrong([pred],test_list[i],[true])
    
with open(output_file,encoding='utf-8',mode='w') as fout:
    for n in range(len(labels)):
        if Z[n] == 0 or Y[n] == 0:
            print(n + 1, X[n], Y[n], Z[n])
            fout.write('class: %s,X:%d,Y:%d,Z:%d\n' % (str(n), X[n], Y[n], Z[n]))
            continue
        f1, precision, recall = 2 * X[n] / (Y[n] + Z[n]), X[n] / Y[n], X[n] / Z[n]
        fout.write('class: %s,X:%d,Y,%d,Z:%d,f1: %.5f, precision: %.5f, recall: %.5f\n' % (
            str(n), X[n], Y[n], Z[n], f1, precision, recall))
        print('class: %s,X:%d,Y,%d,Z:%d,f1: %.5f, precision: %.5f, recall: %.5f\n' % (
            str(n), X[n], Y[n], Z[n], f1, precision, recall))
    # label = "339"
    f1, precision, recall = 2 * sum(X) / (sum(Y) + sum(Z)), sum(X) / sum(Y), sum(X) / sum(Z)
    fout.write('total: %s,X:%d,Y,%d,Z:%d,f1: %.5f, precision: %.5f, recall: %.5f\n' % (
        "total", sum(X), sum(Y), sum(Z), f1, precision, recall))

    # 实体四大类计算
    x_4 = X[7] + X[8] + X[9] + X[14] + X[15]
    y_4 = Y[7] + Y[8] + Y[9] + Y[14] + Y[15]
    z_4 = Z[7] + Z[8] + Z[9] + Z[14] + Z[15]

    f1_4, precision_4, recall_4 = 2 * x_4 / (y_4 + z_4), x_4 / y_4, x_4 / z_4
    print('四大类: %s,X:%d,Y,%d,Z:%d,f1: %.5f, precision: %.5f, recall: %.5f\n' % (
        "total", x_4, y_4, z_4, f1_4, precision_4, recall_4))
    print('total: %s,X:%d,Y,%d,Z:%d,f1: %.5f, precision: %.5f, recall: %.5f' % (
        "total", sum(X), sum(Y), sum(Z), f1, precision, recall))
    fout.write('四大类: %s,X:%d,Y,%d,Z:%d,f1: %.5f, precision: %.5f, recall: %.5f\n' % (
        "total", x_4, y_4, z_4, f1_4, precision_4, recall_4))