import csv
import pickle


class Serializer:

    @staticmethod
    def serialize_csv(file_path, data):
        with open(file_path, 'w', newline="") as file:
            columns = ['numerator', 'denominator']
            writer = csv.DictWriter(file, fieldnames=columns)
            writer.writeheader()
            for num in data:
                writer.writerow(num.value())

    @staticmethod
    def deserialize_csv(file_path):
        data = list()
        with open(file_path, 'r', newline="") as file:
            reader = csv.DictReader(file)
            for row in reader:
                data.append(row)
        return data

    @staticmethod
    def serialize_pickle(file_path, data):
        with open(file_path, 'wb') as file:
            pickle.dump(data, file)

    @staticmethod
    def deserialize_pickle(file_path):
        with open(file_path, 'rb') as file:
            data = pickle.load(file)
        return data
