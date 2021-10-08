import sys
import time
import psutil

def papr(times):
    # get pid from args
    if len(sys.argv) < 2:
        print("missing pid arg")
        sys.exit()

    # get process
    pid = int(sys.argv[1])
    p = psutil.Process(pid)
    count = 1
    with open("Kaspersky" + '_' + str(pid) + ".cvs", "a+") as f:
        f.write("time,cpu%,mem%\n")  # titles
        while count <= times:
            t = time.localtime()
            current_time = '%d:%d:%d' % (t.tm_hour, t.tm_min, t.tm_sec)
            cpu_percent = p.cpu_percent()
            mem = p.memory_percent()

            line = current_time + ',' + str(cpu_percent) + ',' + str(mem)
            print('第{}次采集成功'.format(count))
            f.write(line + "\n")
            time.sleep(1)
            count += 1


if __name__ == "__main__":
    papr(times=4)