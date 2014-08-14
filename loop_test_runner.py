from subprocess import Popen, PIPE
import sys
import time


test_module = sys.argv[1]
test_class = sys.argv[2]
test_method = sys.argv[3]
nb_of_runs = int(sys.argv[4])

TEST_TIMEOUT = 60 # 60s

def wait_for_test_process_to_complete(process):
    timeout = 0
    while timeout < TEST_TIMEOUT:
        if process.poll() == None: # process still alive
            timeout += 1
            time.sleep(1)
        else: # process finished
            return
    return
    

    
def run_tests():
    print "Will run   <%d TIMES>   %s::%s::%s" %(nb_of_runs, test_module, test_class, test_method)
    print "\n"
    for i in range(nb_of_runs):
        cmd = 'py.test %s::%s::%s --resultlog=results\\res_%d.txt' %(test_module, test_class, test_method, i+1)
        running_test_process = Popen(cmd, shell=True, stdout=PIPE)
        wait_for_test_process_to_complete(running_test_process)
        if running_test_process.returncode == 0:
            status = "pass"
        elif running_test_process.returncode == 1:
            status = "FAIL: see results\\res_%s.txt" %(i+1)
        print "Run %d: %s" %(i+1, status)
    print "\n\nDone."


run_tests()