
import os
import numpy as np

def read_files(directory, endswitch='txt'):
    read_files = []
    for filename in os.listdir(directory):
        f = os.path.join(directory, filename)
        if os.path.isfile(f) and f.endswith('txt'):
            read_files.append(f)
    return read_files

def data_validation(file_path, n_peaks):
    file_pointer = open(file_path, "r")
    lines = file_pointer.read().splitlines()
    data_row_list = []
    header_line = None

    print("Validating data in file: {}".format(file_path))

    #check if header is initialized to fetch data
    for n in range(len(lines)):
        line = lines[n]
        if "Timestamp	# CH" in line:
            header_line = n
            continue
        if header_line is not None:
            data_row_list.append(line.split("\t"))
    
    # is there a header after which there should be data?
    if header_line == None:
        raise Exception('The timestamp collumn header was not found, check if file: {} has been initialized'.format(file_path))
    
    # are there data lines after the header?
    if len(data_row_list) == 0:
        raise Exception("No lines of data were loaded in file: {} check if there is data at all".format(file_path))

    # does every row have the correct number of peaks and read into numpy array
    shape = (len(data_row_list), n_peaks)
    wavel_array = np.zeros(shape)
    for row in range(len(data_row_list)):
        peaks = int(data_row_list[row][1])
        line_number = row+1
        if peaks != n_peaks:
            raise Exception("data row {} does not have the stated number of peaks ({} instead of {})".format(line_number, peaks ,n_peaks))
        
        # convert the comma in the string to float
        data_row = data_row_list[row]
        float_row = []
        for col in range(2,len(data_row)):
            data_point = data_row[col]
            float_point = float(data_point.replace(',', '.'))
            float_row.append(float_point)

        wavel_array[row] = np.array(float_row)
    return wavel_array


