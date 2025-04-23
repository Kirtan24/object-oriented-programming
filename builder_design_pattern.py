class Computer:
    def __init__(self, cpu, ram, storage, gpu=None):
        self.cpu = cpu
        self.ram = ram
        self.storage = storage
        self.gpu = gpu

    def __str__(self):
        return f"CPU: {self.cpu}, RAM: {self.ram}, Storage: {self.storage}, GPU: {self.gpu}"

class ComputerBuilder:
    def __init__(self):
        self.cpu = None
        self.ram = None
        self.storage = None
        self.gpu = None

    def set_cpu(self, cpu):
        self.cpu = cpu
        return self

    def set_ram(self, ram):
        self.ram = ram
        return self

    def set_storage(self, storage):
        self.storage = storage
        return self

    def set_gpu(self, gpu):
        self.gpu = gpu
        return self

    def build(self):
        if not self.cpu or not self.ram or not self.storage:
            raise Exception("CPU, RAM and Storage are required")
        return Computer(self.cpu, self.ram, self.storage, self.gpu)

def main():
    computer1 = ComputerBuilder().set_cpu("i7").set_ram("16GB").set_storage("1TB SSD").set_gpu("Nvidia 1080").build()
    print(computer1)

    computer2 = ComputerBuilder().set_cpu("i5").set_ram("8GB").set_storage("500GB HDD").build()
    print(computer2)

    computer3 = ComputerBuilder().set_cpu("i3").set_ram("4GB").build()
    print(computer3)

if __name__ == "__main__":
    main()