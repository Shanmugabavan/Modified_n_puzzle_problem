import random

def print_2_dim_array(arr):
    for i in arr:
        for j in i:
            print(i, end=" ")
        print()

def write_random_input_data(f,possible_values):
    for i in range(3):
        for j in range(3):
            index = random.randint(0, len(possible_values) - 1)
            f.write(f"{possible_values[index]} ")
            del possible_values[index]
        f.write("\n")

def main():
    for i in range(1,101):
        possible_values = ['1','2','3','4','5','6','7','-','-']
        random.seed(i+200)                    #change the seed to 200 when generate output
        with open(f"./goals/{i}.txt", "w") as f:   #when generate goals change it inputs as goals
            write_random_input_data(f,possible_values)


if __name__ == '__main__':
    main()
