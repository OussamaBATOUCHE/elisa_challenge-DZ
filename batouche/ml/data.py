import random


def shuffle(dataset):

    shuffledDS = dataset[:]
    for i in range(len(shuffledDS)):
        # select a random element
        j = int(random.randint(0, (len(shuffledDS)-1)))
        e = shuffledDS[i]
        shuffledDS[i] = shuffledDS[j]
        shuffledDS[j] = e

    return shuffledDS

# print(shuffle([[74,63,0],[75,62,1],[76,67,0],[77,65,3],[78,65,1],[83,58,2]]))


def shuffle_ds(input, target):

    in_ds = input[:]
    for i in range(len(in_ds)):
        in_ds[i].append(target[i])  # [i][a,c,d,e].append(1/0) => [a,c,d,e,1/0]
    shfl_io = shuffle(in_ds)                 # [i+-n][a,c,d,e,1/0]
    new_in = []
    new_tr = []
    for j in range(len(input)):  # [j][a,c,d,e,1/0] => [a,c,d,e],[1/0]
        new_in.append([shfl_io[j][0], shfl_io[j][1], shfl_io[j][2]])
        new_tr.append(shfl_io[j][3])
    print('  --[DATA SHUFFLE]: Done!')
    return [new_in, new_tr]

# print(shuffle_ds([[74,63,0],[75,62,1],[76,67,0],[77,65,3],[78,65,1],[83,58,2]],[1,0,0,1,0,1]))


def data_from_file(path):

    finalDataset = []
    with open(path, "r", encoding="utf-8") as file:
        for line in file:
            line = line.split(",")
            line[5] = line[5].strip('\n')
            # print(line[2]) #delete header
            lon = float(line[2])
            lat = float(line[3])
            day = float(line[4])
            cvre = float(line[5])

            finalDataset.append(
                [lon, lat, day, cvre])
    print("[DATA_FROM_FILE]: Completed!")

    return finalDataset


def preprocessing(path_TrainData, path_TestData, train_perc=0.8):

    data = data_from_file(path_TrainData)
    t_data = data_from_file(path_TestData)
    print(len(data))
    size_data = len(data)
    size_train = int(size_data * train_perc)

    train_input = []
    train_target = []
    valid_input = []
    valid_target = []

    for i in range(1, size_train):  # 1 to skip the header
        train_input.append([data[i][0],
                            data[i][1],
                            data[i][2]
                            ])
        train_target.append(data[i][3])

    for i in range(size_train, size_data):
        valid_input.append([data[i][0],
                            data[i][1],
                            data[i][2]
                            ])
        valid_target.append(data[i][3])

    test_input = []
    test_target = []
    for i in range(len(t_data)):
        test_input.append([data[i][0],
                           data[i][1],
                           data[i][2]
                           ])
        test_target.append(t_data[i][3])

    return [train_input, train_target, valid_input, valid_target, test_input, test_target]


# x, y, r, e, z, d = preprocessing("dataset/haberman.data", "dataset/test_01.data", 0.8)
# print(x)
# dataset = preprocessing(
#     "dataset/data_normalized.csv", "dataset/test.data", 0.8)
