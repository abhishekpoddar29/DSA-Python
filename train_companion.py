def find_companion(berth):
    comp=(berth-1)//8+1
    pos=(berth-1)%8+1

    comp_map={1:4, 2:5 , 3:6,4:1,5:2,6:3, 7:8,8:7}
    berth_map={1:"LB", 2:"MB",3:"UB",4:"LB",5:"MB",6:"UB",7:"SL",8:"SU"}
    companion_pos=comp_map[pos]
    companion_seat=(comp-1)*8+companion_pos
    berth_type=berth_map[pos]
    companion_berth_type=berth_map[companion_pos]

    return companion_seat,companion_berth_type
T=int(input())
for i in range(T):
    N=int(input())
    comp_seat,comp_berth_type=find_companion(N)
    print((comp_seat) (comp_berth_type))