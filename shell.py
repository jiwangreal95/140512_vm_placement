import os

file_dir = "input/vm_flow_matrix/"
#file_list = os.listdir(file_dir)
file_list = ["1Partition@15.data"]
#methods = [" -a ", " -n ", " -h ", " -z "]
methods = [" -b "]

for filename in file_list:
    for method in methods:
        print filename + "\ting....."
        '''print "method: " + method
        cmd1 = "h:/PYTHON26/python.exe 1_MC_BT_algorithm.py " + file_dir + filename + method
        #  + " > test/" + filename +"_test1.txt" 
        os.system(cmd1)
        '''
        cmd1 = "h:/PYTHON26/python.exe 1_handle_cluster_result.py " + filename
        #  + " > test/" + filename +"_test1.txt" 
        os.system(cmd1)
        
        cmd2 = "h:/PYTHON26/python.exe 2_BF_algorithm.py " + file_dir + filename
        # + " > test/" + filename +"_test2.txt"
        os.system(cmd2)


