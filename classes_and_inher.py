import csv
import os

def validate(row):
    if len(row) != 7:
        return False
    if (row[1] == '') or (row[3] == '') or (row[5] == ''):
        return False

    ext = os.path.splitext(row[3])[-1]
    if not ((ext=='.jpg') or (ext=='.jpeg') or (ext=='.png') or (ext=='.gif')):
        return False
    
    if row[0] == 'car':
        if (row[2] == ''):
            return False
    elif row[0] == 'truck':
        pass
    elif row[0] == 'spec_machine':
        if (row[6] == ''):
            return False
    else:
        return False

    return True

class CarBase:
    def __init__(self, brand, photo_file_name, carrying):
        self.brand = brand
        self.photo_file_name = photo_file_name
        self.carrying = float(carrying)
    
    def get_photo_file_ext(self):
        return os.path.splitext(self.photo_file_name)[-1]


class Car(CarBase):
    def __init__(self, brand, photo_file_name, carrying, passenger_seats_count):
        super().__init__(brand, photo_file_name, carrying)
        self.car_type = 'car'
        self.passenger_seats_count = int(passenger_seats_count)


class Truck(CarBase):
    def __init__(self, brand, photo_file_name, carrying, body_lwh):
        super().__init__(brand, photo_file_name, carrying)
        self.car_type = 'truck'
        self.body_lwh = body_lwh
        lwh = body_lwh.split('x')
        try:
            if len(lwh) == 3:
                self.body_length = float(lwh[0])
                self.body_width = float(lwh[1])
                self.body_height = float(lwh[2])
            else:
                self.body_length = 0.0
                self.body_width = 0.0
                self.body_height = 0.0

        except ValueError:
            self.body_length = 0.0
            self.body_width = 0.0
            self.body_height = 0.0

    def get_body_volume(self):
        return self.body_length*self.body_width*self.body_height


class SpecMachine(CarBase):
    def __init__(self, brand, photo_file_name, carrying, extra):
        super().__init__(brand, photo_file_name, carrying)
        self.car_type = 'spec_machine'
        self.extra = extra


def get_car_list(csv_filename):
    car_list = []
    with open(csv_filename) as csv_fd:
        reader = csv.reader(csv_fd, delimiter=';')
        next(reader)  # пропускаем заголовок
        for row in reader:
            if validate(row):
                if row[0] == 'car':
                    car_list.append(Car(row[1], row[3], row[5], row[2]))
                if row[0] == 'truck':
                    car_list.append(Truck(row[1], row[3], row[5], row[4]))
                if row[0] == 'spec_machine':
                    car_list.append(SpecMachine(row[1], row[3], row[5], row[6]))
    csv_fd.close()
    return car_list


def main():
    cars = get_car_list('coursera_cars.csv')
    print(cars)

if __name__=='__main__':
    main()
