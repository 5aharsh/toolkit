import subprocess, gc

class Tasks:
    def view(self):
        return subprocess.check_output("tasklist /nh | sort /+1", shell=True).decode('utf-8')
    
    def full_view(self, search, sort):
        tasklist = self.view().split('\n')
        print("%-35s %-8s %-10s %-11s"%("Process", "ID", "Session", "Memory (KB)"))
        print("%-35s %-8s %-10s %-11s"%("="*35, "="*8, "="*10, "="*10))

        tasks = []

        for i in tasklist:
            a = list(filter(('').__ne__, i.split(' ')))
            if len(a)==6:
                tasks.append([a[0], int(a[1]), a[2], a[3], int(a[4].replace(",", ""))])
        if sort=="id":
            tasks.sort(key=lambda x:x[1])
        elif sort=="session":
            tasks.sort(key=lambda x:x[2])
        elif sort=="memory":
            tasks.sort(key=lambda x:x[4], reverse=True)

        for a in tasks:
            if search:
                if search.lower() in a[0].lower() or a[1]==search:
                    print("%-35s %-8s %-10s %-11s"%(a[0], a[1], a[2], a[4]))
            else:
                print("%-35s %-8s %-10s %-11s"%(a[0], a[1], a[2], a[4]))

    def short_view(self, search, sort):
        tasklist = self.view().split('\n')
        tasks = {}
        for i in tasklist:
            a = list(filter(('').__ne__, i.split(' ')))
            if len(a)==6:
                if a[0] in tasks.keys():
                    # something
                    tasks[a[0]]["memory"] += int(a[4].replace(',', ''))
                    tasks[a[0]]["sub"] += 1
                    if not a[2]==tasks[a[0]]["session"]:
                        tasks[a[0]]["session"] = "-"
                else:
                    tasks[a[0]] = {
                        "session": a[2],
                        "memory": int(a[4].replace(',', '')),
                        "sub": 1
                    }
        print("%-30s %-20s %-11s %-14s"%("Process", "Session", "Memory (KB)", "# of Processes"))
        print("%-30s %-20s %-11s %-14s"%("="*30, "="*20, "="*10, "="*14))
        tasklist = []
        gc.collect()
        for i in tasks:
            tasklist.append([i, tasks[i]["session"], tasks[i]["memory"], tasks[i]["sub"]])
        if sort=="session":
            tasklist.sort(key=lambda x:x[1])
        elif sort=="memory":
            tasklist.sort(key=lambda x:x[2], reverse=True)
        for i in tasklist:
            if search:
                if search.lower() in i[0].lower():
                    print("%-30s %-20s %-11i %-14s"%(i[0], i[1], i[2], i[3]))
            else:
                print("%-30s %-20s %-11i %-14s"%(i[0], i[1], i[2], i[3]))