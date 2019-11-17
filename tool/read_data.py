import yaml


class ReadData:
    # 1.读取文件
    def read_yaml(self, filename):
        with open("./data/{}".format(filename), "rb") as f:
            return yaml.load(f)

    # 2.返回符合需求的数据
    def get_data(self, filename):
        data = []
        for value in self.read_yaml(filename).values():
            data.append(tuple(value.values()))
        return data

if __name__ == '__main__':
    data = ReadData().get_data("mp_login.yaml")
    print(data)


