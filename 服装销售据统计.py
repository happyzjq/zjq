'''
全年的销售总额
每种衣服的销售（件数）占比
每种衣服的月销售（件数）占比
每种衣服的销售额占比

最畅销的衣服是那种
每个季度最畅销的衣服
全年销量最低的衣服


'''
import xlrd

wb = xlrd.open_workbook(filename=r"E:\python自动化测试\Python阶段三\day09【excel表】\2020年每个月的销售情况.xlsx")
# 整体存储数据库
store = {}


table = wb.sheet_names()

for i in table:
    #获取选项卡
    sheet = wb.sheet_by_name(i)

    #获取有多少航
    nrow =sheet.nrows

    for j in range(1,nrow):
        #获取第J行数据
        data = sheet.row_values(j)
        if data[1] in store:
            store[data[1]]={
               "sum":round(store[data[1]]["sum"] + data[2]*data[4],2),
                "count":int(store[data[1]]["count"] +data[4])
            }
        else:
            store[data[1]] = {
                "sum":round(data[2]*data[4],2),
                "count":int(data[4])
            }
all_money = sum(store[k]["sum"] for k in store)
all_num = sum(store[k]["count"] for k in store)
print("全年销售总额：%s￥" % round(all_money,2))
print("全年总销售量：%s件" % round(all_num,2))
for name in store:
    print("-------------------------")
    print("%s的销售额占比为：%s" % (name,round(store[name]["sum"] / all_money * 100,2)),"%")
    print("%s的销售量占比为：%s" % (name,round(store[name]["count"] / all_num * 100,2)),"%")


