from prettytable import PrettyTable

def Show_DB(re_data):
    col = []
    table_data = []
    data = re_data
    if len(data) != 0:
        col = list(data[0].keys())
        # print(col)
        # print(len(data)) # 반환된 데이터 갯수 체크 --> 첫 분기를 위한 조건

        # for d in data:
        #     table_data.append(list(d.values()))
        #     print(list(d.values()))

        t = PrettyTable(col)
        resultList = []
        

        for row in data:
            d = list(row.values())
            # print(d)
            t.add_row(d)
            resultList.append(d) 
        print(t)
        return resultList
    else:
        col = ["No Result"]
        print(t)
        return []

#쿼리문
# # SELECT * from Customer

# 결과
# status cod: [{
#     'seller_id': 1,
#     'name': 'Whang',
#     'phone': '010-2222-0000',
#     'store': 'Boramae'
# }, {
#     'seller_id': 2,
#     'name': 'Curry',
#     'phone': '010-2222-1111',
#     'store': 'Jamsil'
# }, {
#     'seller_id': 3,
#     'name': 'Irving',
#     'phone': '010-2222-3333',
#     'store': 'Boramae'
# }, {
#     'seller_id': 4,
#     'name': 'Green',
#     'phone': '010-2222-2222',
#     'store': 'Boramae'
# }, {
#     'seller_id': 5,
#     #'name': 'Mathal',
#     'phone': '010-2222-4444',
#     'store': 'Boramae'
# }, {
#     'seller_id': 6,
#     'name': 'Wood',
#     'phone': '010-2222-5555',
#     'store': 'Boramae'
# }, {
#     'seller_id': 7,
#     'name': 'Sergio',
#     'phone': '010-2222-6666',
#     'store': 'Jamsil'
# }, {
#     'seller_id': 8,
#     'name': 'Roberto',
#     'phone': '010-2222-7777',
#     'store': 'Jamsil'
# }, {
#     'seller_id': 9,
#     'name': 'John',
#     'phone': '010-2222-8888',
#     'store': 'Jamsil'
# }, {
#     'seller_id': 10,
#     'name': 'Jony',
#     'phone': '010-2222-9999',
#     'store': 'Jamsil'
# }, {
#     'seller_id': 11,
#     'name': 'Alice',
#     'phone': '010-2222-1010',
#     'store': 'Boramae'
# }]

"""
<LOGIC>
- DB 쿼리 데이터를 출력할 시 반드시 SELECT 문을 통해서 데이터를 가져와야 하며 위와 같은 결과를 가진다.
- 반환되는 Data값은 튜플 리스트 형태

[SHOW DB 함수에 리스트 형태로 넘기기]
- 첫번째 요소에서 column 값으로 사용할 내용을 뽑아낸다 --> Beautiful Table에서 column으로 사용할 것
        - 각 요소는 dict 타입으로 되어있어 key값을 뽑아내 사용한다.
- 만약 반환값이 없는 경우 --> 검색값이 0개일 경우 예외 처리 : 빈 테이블에 column을 한개로 처리하고 No Result라고 뜨게 한다.
                    -->  ShowDB의 반환값인 resultList도 빈 리스트를 반환하도록 한다.

"""
data = [{
    'seller_id': 1,
    'name': 'Whang',
    'phone': '010-2222-0000',
    'store': 'Boramae'
}, {
    'seller_id': 2,
    'name': 'Curry',
    'phone': '010-2222-1111',
    'store': 'Jamsil'
}, {
    'seller_id': 3,
    'name': 'Irving',
    'phone': '010-2222-3333',
    'store': 'Boramae'
}, {
    'seller_id': 4,
    'name': 'Green',
    'phone': '010-2222-2222',
    'store': 'Boramae'
}, {
    'seller_id': 5,
    'name': 'Mathal',
    'phone': '010-2222-4444',
    'store': 'Boramae'
}, {
    'seller_id': 6,
    'name': 'Wood',
    'phone': '010-2222-5555',
    'store': 'Boramae'
}, {
    'seller_id': 7,
    'name': 'Sergio',
    'phone': '010-2222-6666',
    'store': 'Jamsil'
}, {
    'seller_id': 8,
    'name': 'Roberto',
    'phone': '010-2222-7777',
    'store': 'Jamsil'
}, {
    'seller_id': 9,
    'name': 'John',
    'phone': '010-2222-8888',
    'store': 'Jamsil'
}, {
    'seller_id': 10,
    'name': 'Jony',
    'phone': '010-2222-9999',
    'store': 'Jamsil'
}, {
    'seller_id': 11,
    'name': 'Alice',
    'phone': '010-2222-1010',
    'store': 'Boramae'
}]

# data[0] --> {
#     'seller_id': 1,
#     'name': 'Whang',
#     'phone': '010-2222-0000',
#     'store': 'Boramae'
# }
# table_data = []
# column = list(data[0].keys())

# print(len(data)) # 반환된 데이터 갯수 체크 --> 첫 분기를 위한 조건

# for d in data:
#     table_data.append(list(d.values()))

# print(table_data)


Show_DB(data)
Show_DB({[]})