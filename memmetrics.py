import psutil
from psutil._common import bytes2human

# Function to store and order the result as an integer data type
def pprint_ntuple(nt):
    for name in nt._fields:
        value = getattr(nt, name)
        if name != 'percent':
            value = int(value)
        print('%-10s : %7s' % (name.capitalize(), value))

# Function to print the result of memory metrics
def main():
    print('\nMEMORY\n------')
    print('\nVirtual memory\n--------------')
    print('---------   ---------')
    pprint_ntuple(psutil.virtual_memory())
    print('---------   ---------')
    print('\nSWAP\n----')
    print('---------   ---------')
    pprint_ntuple(psutil.swap_memory())
    print('---------   ---------')


if __name__ == '__main__':
    main()
