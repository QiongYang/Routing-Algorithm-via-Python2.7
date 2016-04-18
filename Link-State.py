import sys

class Vertex:
    def __init__(self, node):
        self.id = node
        self.adjacent = {}
        # Set distance to infinity for all nodes
        self.distance = sys.maxint
        # Mark all nodes unvisited        
        self.visited = False  
        # Predecessor
        self.previous = None

    def add_neighbor(self, neighbor, weight=0):
        self.adjacent[neighbor] = weight

    def get_connections(self):
        return self.adjacent.keys()  

    def get_id(self):
        return self.id

    def get_weight(self, neighbor):
        return self.adjacent[neighbor]

    def set_distance(self, dist):
        self.distance = dist

    def get_distance(self):
        return self.distance

    def set_previous(self, prev):
        self.previous = prev

    def set_visited(self):
        self.visited = True

    def __str__(self):
        return str(self.id) + ' adjacent: ' + str([x.id for x in self.adjacent])

class Graph:
    def __init__(self):
        self.vert_dict = {}
        self.num_vertices = 0

    def __iter__(self):
        return iter(self.vert_dict.values())

    def add_vertex(self, node):
        self.num_vertices = self.num_vertices + 1
        new_vertex = Vertex(node)
        self.vert_dict[node] = new_vertex
        return new_vertex

    def get_vertex(self, n):
        if n in self.vert_dict:
            return self.vert_dict[n]
        else:
            return None

    def add_edge(self, frm, to, cost = 0):
        if frm not in self.vert_dict:
            self.add_vertex(frm)
        if to not in self.vert_dict:
            self.add_vertex(to)

        self.vert_dict[frm].add_neighbor(self.vert_dict[to], cost)
        self.vert_dict[to].add_neighbor(self.vert_dict[frm], cost)

    def get_vertices(self):
        return self.vert_dict.keys()

    def set_previous(self, current):
        self.previous = current

    def get_previous(self, current):
        return self.previous

def shortest(v, path):
    ''' make shortest path from v.previous'''
    if v.previous:
        path.append(v.previous.get_id())
        shortest(v.previous, path)
    return

import heapq

def dijkstra(aGraph, start):
    print '''Dijkstra's shortest path is'''
    # Set the distance for the start node to zero 
    start.set_distance(0)

    # Put tuple pair into the priority queue
    unvisited_queue = [(v.get_distance(),v) for v in aGraph]
    heapq.heapify(unvisited_queue)

    while len(unvisited_queue):
        # Pops a vertex with the smallest distance 
        uv = heapq.heappop(unvisited_queue)
        current = uv[1]
        current.set_visited()

        #for next in v.adjacent:
        for next in current.adjacent:
            # if visited, skip
            if next.visited:
                continue
            new_dist = current.get_distance() + current.get_weight(next)

            
            if new_dist < next.get_distance():
                next.set_distance(new_dist)
                next.set_previous(current)
                
        while len(unvisited_queue):
            heapq.heappop(unvisited_queue)
        # 2. Put all vertices not visited into the queue
        unvisited_queue = [(v.get_distance(),v) for v in aGraph if not v.visited]
        heapq.heapify(unvisited_queue)


if __name__ == '__main__':

    g = Graph()
    lines = ['FujinRd','WestYouyiRd','BaoanHighway','Gongfuxincun' ,'HulanRd','Tonghexincun',
    'GongkangRd', 'Pengpuxincun', 'WenshuiRd', 'ShanghaiCircusWorld','YanchangRd', 
    'NorthZhongshanRd', 'ShanghaiRailwayStation', 'HanzhongRd', 'XinzhaRd', 'PeoplesSquare', 
    'SouthHuangpiRd', 'SouthShanxiRd', 'ChangshuRd', 'HengshanRd', 'Xujiahui', 
    'ShanghaiIndoorStadium', 'CaobaoRd', 'ShanghaiSouthRailwayStation', 'JinjiangPark', 
    'LianhuaRd', 'WaihuanRd', 'Xinzhuang',
    'EastXujing','HongqiaoRailwayStation','HongqiaoAirportT2','SonghongRd',
    'Beixinjing','XianningRd','LoushanguanRd','ZhongshanPark','JiangsuRd','JinganTemple',
    'WestNanjingRd''EastNanjingRd','Lujiazui','DongchangRd','CenturyAvenue',
    'ShanghaiScience&TechnologyMuseum','CenturyPark','LongyangRd','ZhangjiangHighTechPark',
    'JinkeRd', 'GuanglanRd','Tangzhen','MiddleChuangxinRd','EastHuaxiaRd','Chuansha',
    'LingkongRd','YuandongAvenue','HaitiansanRd','PudongInternationalAirport',
    'Shanghai South Railway Station','Shilong Rd','Longcao Rd','Caoxi Rd','Yishan Rd',
    'Hongqiao Rd','West Yanan Rd','Jinshajiang Rd','Caoyang Rd','Zhengping Rd',
    'Zhongtan Rd','Baoshan Rd','Donbaoxing Rd','Hongkou footballium','Chifeng Rd',
    'Dabaishu','Jiangwan Town','West Yingao Rd','South Changjiang Rd','Songfa Rd','Zhanghuabang',
    'Songbin Rd','Shuichan Rd','Baoyang Rd','Youyi Rd','Tieli Rd','North Jiangyang Rd',
    'Shanghai Stadium','Dongan Rd','Damuqiao Rd','Luban Rd','South Xizang Rd','Nanpu Bridge','Tangqiao',
    'Lancun Rd','Pudian4 Rd','Pudong Avenue','Yangpu Rd','Dalian Rd','Linping Rd','Hailun Rd',
    'Chunshen Rd','Yindu Rd','Zhuanqiao','Beiqiao','Jianchuan Rd','Dongchuan Rd',
    'Jinping Rd','Huaning Rd','Wenjing Rd','Mihang Development Zone',
    'Gangcheng Rd','North Waigaoqiao Free Trade Zone','Hangjin Rd','South Waigaoqiao Free Trade Zone',
    'Zhouhai Rd','Wuzhou Avenue','Dongjing Rd','Jufeng Rd','Wulian Rd','Boxing Rd','Jinqiao Rd','Yunshan Rd',
    'Deping Rd','Beiyangjing Rd','Minsheng Rd','Yuanshen Stadium','Pudian6 Rd','Shanghai Children Medical Center',
    'Linyi Xincun','West Gaoke Rd','Dongming Rd','Gaoqing Rd','West Huaxia Rd','Shangnan Rd','South Lingyan Rd','Oriental Sports Center',
    'Huamu Rd','Fanghua Rd','Jinxiu Rd','South Yanggao Rd','Yuntai Rd','Yaohua Rd',
    'Changqing Rd','Houtan','Middle Longhua Rd','Zhaojiabang Rd','Changping Rd',
    'Changshou Rd','Langao Rd','Xincun Rd','Dahuasan Rd','Xingzhi Rd','Dachang Town',
    'Changzhong Rd','Shangda Rd','Nanchen Rd','Shanghai University','Guncun Park','Luonan Xincun','Meilan Lake',
    'Shendu Highway','Lianhang Rd','Jiangyue Rd','Pujiang Town','Luheng Rd','Linzhao Xincun','Yangsi',
    'Chengshan Rd','China Art Museum','LUjiabang Rd','Laoximen','Dashijie','Qufu Rd',
    'Zhongxing Rd','North Xizang Rd','Quyang Rd','Siping Rd','Anshan Xincun','Jiangpu Rd',
    'Huangxing Rd','Middle Yanji Rd','Huangxing Park','Yangyin Rd','Nengjiang Rd','Shiguang Rd','Middle Yanggao Rd','Shangchen Rd','Xiaonanmen','Madang Rd','Dapuqiao','Jianshan Rd','Guilin Rd',
    'Caohejing Development Zone','Hechuan Rd','Xingzhong Rd','Qibao','Zhongchun Rd','Jiuting','Sijing',
    'Shenshan','Dongjing','Songjiang University Town','Songjiang Xincheng','Songjiang Stadium',
    'Zuibaichi','South Songjiang Railway Station',
    'Xinjiangwancheng','East Yingao Rd','Sanmen Rd','Jiangwan Stadium','Wujiaochang','Guoquan Rd',
    'Tongji University','Youdian Xincun','North Sichuan Rd','Tiantong Rd','Yuyuan','Xintiandi',
    'Shanghi Library','Jiaotong University','Songyuan Rd','Yili Rd','Shuicheng Rd','Longxi Rd',
    'Shanghai Zoo','Hongqiao Airport T1','Longbai Xincun','Ziteng Rd','Hangzhong Rd',
    'Kangxin Highway','Xiuyan Rd','Luoshan Rd','Yuqiao','Pushan Rd','East Sanlin','Sanlin','Longyao Rd',
    'Yunjin Rd','Longhua','Shanghai Swimming Center','Longde Rd','Fengqiao Rd','Zhengru',
    'West Shanghai Railway Station','Liziyuan','Qianlianshan Rd','Wuwei Rd','Taopu Xincun','Nanxiang',
    'Malu','Jiading Xincheng','Baiyin Rd','West Jiading Railway Station','North Jiading Railway Station',
    'Shanghai  Circuit','East Changji  Rd','Shanghai Automobile City','Anting','Zhaofen Rd','Guangming Rd','Huaqiao',
    'Jinhai Rd','Shenjiang Rd','Jinjing Rd','North Yanggao Rd','Donglu Rd','Fuxing Island','Aiguo Rd','Longchang Rd',
    'Lingguo Rd','Jiangpu Park','Tilanqiao','International  Passenger Transportation Center','Guilin Park','Hongcao Rd',
    'Hongmei Rd','Donglan Rd','Gudai Rd','Hongxin Rd','Qixing Rd',
    'Jingyun Rd','West Jinshajiang Rd','Fengzhuang','South Qianlianshan Rd','Zhenbei Rd','Daduhe Rd','Wuning Rd','Jiangning Rd',
    'Natural Museum','Middle Huaihai Rd','World Exposition Museum','Exposition Avenue',
    'Dishui Lake','Lingang Avenue','Shuyuan','East Huinan','Huinan','Safari Park','Xinchang','East Hangtou','Heshahangcheng','East Zhoupu','Middle Huaxia Rd']
    for station in lines:
        stations = g.add_vertex(station)
    line1=[]
    for i in range(28):
    	line1.append(lines[i])
    delay1 = [2,2,3,3,2,3,2,3,3,2,2,3,1,2,2,3,2,2,2,2,3,2,3,3,3,3,3]
    #print g.stations
    for i in range(27):
        g.add_edge(line1[i],line1[i+1],delay1[i])
    #print g.edges
    line2 = ['EastXujing','HongqiaoRailwayStation','HongqiaoAirportT2','SonghongRd',
    'Beixinjing','XianningRd','LoushanguanRd','ZhongshanPark','JiangsuRd','JinganTemple',
    'WestNanjingRd']+[line1[15]]+['EastNanjingRd','Lujiazui','DongchangRd','CenturyAvenue',
    'ShanghaiScience&TechnologyMuseum','CenturyPark','LongyangRd','ZhangjiangHighTechPark',
    'JinkeRd', 'GuanglanRd','Tangzhen','MiddleChuangxinRd','EastHuaxiaRd','Chuansha',
    'LingkongRd','YuandongAvenue','HaitiansanRd','PudongInternationalAirport']

    delay2 = [3,2,7,2,2,3,3,2,3,2,3,2,3,2,2,3,2,2,4,3,2,12,3,4,3,5,5,7,3]
    for i in range(29):
        g.add_edge(line2[i],line2[i+1],delay2[i])
    #print g.stations
    #print g.edges
    line3 = ['Shanghai South Railway Station','Shilong Rd','Longcao Rd','Caoxi Rd','Yishan Rd',
    'Hongqiao Rd','West Yanan Rd']+[line2[7]]+['Jinshajiang Rd','Caoyang Rd','Zhengping Rd',
    'Zhongtan Rd']+[line1[12]]+['Baoshan Rd','Donbaoxing Rd','Hongkou footballium','Chifeng Rd',
    'Dabaishu','Jiangwan Town','West Yingao Rd','South Changjiang Rd','Songfa Rd','Zhanghuabang',
    'Songbin Rd','Shuichan Rd','Baoyang Rd','Youyi Rd','Tieli Rd','North Jiangyang Rd']
    delay3=[2,3,2,2,2,3,2,2,2,3,2,3,3,2,3,2,2,3,2,3,2,3,2,2,3,2,2,3]
    for i in range(28):
        g.add_edge(line3[i],line3[i+1],delay3[i])
    #print g.edges
    line4 = [line3[4]]+[line1[21]]+['Shanghai Stadium','Dongan Rd','Damuqiao Rd','Luban Rd','South Xizang Rd',
    'Nanpu Bridge','Tangqiao','Lancun Rd','Pudian4 Rd']+[line2[15]]+['Pudong Avenue','Yangpu Rd','Dalian Rd',
    'Linping Rd','Hailun Rd']+[line3[13]]+[line3[12]]+[line3[11]]+[line3[10]]+[line3[9]]+[line3[8]]+[line3[7]]+[line3[6]]+[line3[5]]
    delay4=[3,2,2,1,2,3,2,3,2,2,2,3,2,2,3,2,3,3,3,2,3,1,3,2,2]
    #print g.stations
    for i in range(25):
        g.add_edge(line4[i],line4[i+1],delay4[i])
    #print g.edges
    g.add_edge(line3[4],line3[5],2)
    #print g.edges
    line5 = [line1[27]]+['Chunshen Rd','Yindu Rd','Zhuanqiao','Beiqiao','Jianchuan Rd','Dongchuan Rd',
    'Jinping Rd','Huaning Rd','Wenjing Rd','Mihang Development Zone']
    delay5=[2,2,4,3,3,2,3,2,3,2]
    for i in range(10):
        g.add_edge(line5[i],line5[i+1],delay5[i])
    #print g.edges

    line6 = ['Gangcheng Rd','North Waigaoqiao Free Trade Zone','Hangjin Rd','South Waigaoqiao Free Trade Zone',
    'Zhouhai Rd','Wuzhou Avenue','Dongjing Rd','Jufeng Rd','Wulian Rd','Boxing Rd','Jinqiao Rd','Yunshan Rd',
    'Deping Rd','Beiyangjing Rd','Minsheng Rd','Yuanshen Stadium']+[line2[15]]+['Pudian6 Rd']+[line4[9]]+['Shanghai Children Medical Center',
    'Linyi Xincun','West Gaoke Rd','Dongming Rd','Gaoqing Rd','West Huaxia Rd','Shangnan Rd','South Lingyan Rd','Oriental Sports Center']
    delay6=[2,3,3,3,2,2,2,2,3,2,2,3,2,2,3,2,3,2,3,2,3,2,3,2,2,2,2]
    for i in range(27):
        g.add_edge(line6[i],line6[i+1],delay6[i])
    #print g.edges
    line7 = ['Huamu Rd']+[line2[18]]+['Fanghua Rd','Jinxiu Rd','South Yanggao Rd']+[line6[21]]+['Yuntai Rd','Yaohua Rd',
    'Changqing Rd','Houtan','Middle Longhua Rd']+[line4[3]]+['Zhaojiabang Rd']+[line1[18]]+[line2[9]]+['Changping Rd',
    'Changshou Rd']+[line3[10]]+['Langao Rd','Xincun Rd','Dahuasan Rd','Xingzhi Rd','Dachang Town',
    'Changzhong Rd','Shangda Rd','Nanchen Rd','Shanghai University','Guncun Park','Luonan Xincun','Meilan Lake']
    delay7=[3,2,3,2,3,2,2,2,2,3,2,2,3,2,3,2,2,3,2,2,2,2,3,2,2,3,6,9,2]
    for i in range(29):
        g.add_edge(line7[i],line7[i+1],delay7[i])
    #print g.edges
    line8 = ['Shendu Highway','Lianhang Rd','Jiangyue Rd','Pujiang Town','Luheng Rd','Linzhao Xincun']+[line6[27]]+['Yangsi',
    'Chengshan Rd']+[line7[7]]+['China Art Museum']+[line4[6]]+['LUjiabang Rd','Laoximen','Dashijie']+[line1[15]]+['Qufu Rd',
    'Zhongxing Rd','North Xizang Rd']+[line3[15]]+['Quyang Rd','Siping Rd','Anshan Xincun','Jiangpu Rd',
    'Huangxing Rd','Middle Yanji Rd','Huangxing Park','Yangyin Rd','Nengjiang Rd','Shiguang Rd']
    delay8=[2,2,2,4,3,4,2,2,2,2,3,2,2,2,2,2,2,3,2,3,2,2,2,2,2,2,2,2,2]
    for i in range(29):
        g.add_edge(line8[i],line8[i+1],delay8[i])
    line9=['Middle Yanggao Rd']+[line2[15]]+['ShangchenRd','Xiaonanmen']+[line8[12]]+['Madang Rd',
    'Dapuqiao','Jianshan Rd']+[line7[12]]+[line1[20]]+[line3[4]]+['Guilin Rd','Caohejing Development Zone','Hechuan Rd',
    'Xingzhong Rd','Qibao','Zhongchun Rd','Jiuting','Sijing','Shenshan','Dongjing','Songjiang University Town','Songjiang Xincheng',
    'Songjiang Stadium','Zuibaichi','South Songjiang Railway Station']
    delay9=[4,2,4,3,2,2,2,2,3,3,3,3,2,3,3,3,4,6,5,3,4,4,3,3,3]
    for i in range(25):
        g.add_edge(line9[i],line9[i+1],delay9[i])
    line10 = ['Xinjiangwancheng','East Yingao Rd','Sanmen Rd','Jiangwan Stadium','Wujiaochang','Guoquan Rd',
    'Tongji University']+[line8[21]]+['Youdian Xincun']+[line4[16]]+['North Sichuan Rd',
    'Tiantong Rd']+[line2[12]]+['Yuyuan']+[line8[13]]+['Xintiandi']+[line1[17]]+['Shanghi Library',
    'Jiaotong University']+[line3[15]]+['Songyuan Rd','Yili Rd','Shuicheng Rd','Longxi Rd','Shanghai Zoo',
    'Hongqiao Airport T1']+[line2[2]]+[line2[1]]
    delay10=[1,2,2,2,2,2,2,2,2,2,2,3,2,2,2,3,2,2,3,2,1,3,2,2,3,3]
    for i in range(26):
        g.add_edge(line10[i],line10[i+1],delay10[i])
    line11=['Kangxin Highway','Xiuyan Rd','Luoshan Rd','Yuqiao','Pushan Rd','East Sanlin','Sanlin']+[line6[27]]+['Longyao Rd',
    'Yunjin Rd','Longhua','Shanghai Swimming Center']+[line1[20]]+[line10[18]]+[line2[8]]+['Longde Rd']+[line3[9]]+['Fengqiao Rd',
    'Zhengru','West Shanghai Railway Station','Liziyuan','Qianlianshan Rd','Wuwei Rd','Taopu Xincun','Nanxiang','Malu','Jiading Xincheng',
    'Baiyin Rd','West Jiading Railway Station','North Jiading Railway Station','Shanghai Circuit','East Changji  Rd','Shanghai Automobile City',
    'Anting','Zhaofen Rd','Guangming Rd','Huaqiao']
    delay11=[2,2,3,5,3,2,5,3,2,2,3,3,3,3,2,2,2,2,3,2,3,2,2,5,3,3,4,2,4]
    for i in range (29):
        g.add_edge(line11[i],line11[i+1],delay11[i])
    g.add_edge(line11[26],line11[30],2)
    g.add_edge(line11[30],line11[31],5)
    g.add_edge(line11[31],line11[32],3)
    g.add_edge(line11[32],line11[33],2)
    g.add_edge(line11[33],line11[34],2)
    g.add_edge(line11[34],line11[35],3)
    g.add_edge(line11[35],line11[36],2)
    line12=['Jinhai Rd','Shenjiang Rd','Jinjing Rd','North Yanggao Rd']+[line6[7]]+['Donglu Rd','Fuxing Island',
    'Aiguo Rd','Longchang Rd','Lingguo Rd','Jiangpu Park']+[line4[14]]+['Tilanqiao',
    'International  Passenger Transportation Center','International  Passenger Transportation Center']+[line10[11]]+[line8[16]]+[line1[13]]+[line2[10]]+[line1[17]]+[line9[7]]+[line4[4]]+[line7[10]]+[line11[10]]+[line3[2]]+[line1[22]]+['Guilin Park',
    'Hongcao Rd','Hongmei Rd','Donglan Rd','Gudai Rd','Hongxin Rd','Qixing Rd']
    delay12=[4,2,2,3,2,3,2,3,3,2,2,2,2,3,3,3,3,3,2,3,2,3,3,2,2,2,3,2,3,2,2]
    for i in range(31):
        g.add_edge(line12[i],line12[i+1],delay12[i])
    line13=['Jingyun Rd','West Jinshajiang Rd','Fengzhuang','South Qianlianshan Rd','Zhenbei Rd',
    'Daduhe Rd']+[line3[8]]+[line11[15]]+['Wuning Rd']+[line7[16]]+['Jiangning Rd']+[line1[13]]+['Natural Museum']+[line2[10]]+['Middle Huaihai Rd']+[line10[15]]+[line9[5]]+['World Exposition Museum','Exposition Avenue']
    delay13=[2,4,3,2,3,4,2,3,2,2,3,1,3,2,3,2,2,3]
    for i in range(18):
        g.add_edge(line13[i],line13[i+1],delay13[i])
    line16=['Dishui Lake','Lingang Avenue','Shuyuan','East Huinan','Huinan','Safari Park','Xinchang','East Hangtou',
    'Heshahangcheng','East Zhoupu']+[line11[2]]+['Middle Huaxia Rd']+[line2[18]]
    delay16=[3,6,9,5,8,7,6,4,6,7,4,5]
    for i in range(12):
        g.add_edge(line16[i],line16[i+1],delay16[i])

    

    initial_station = raw_input("please input the sorce station: ")
    final_station = raw_input("please input the end station: ")
    dijkstra(g, g.get_vertex(initial_station))
    target = g.get_vertex(final_station)
    #dijkstra(g, g.get_vertex('Zhaojiabang Rd'))
    #target = g.get_vertex('ZhangjiangHighTechPark')
    path = [target.get_id()]
    shortest(target, path)
    cost = target.get_distance()
    print '%s' %(path[::-1])
    print 'The time cost is %d' %(cost)
