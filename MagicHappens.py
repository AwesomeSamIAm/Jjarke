def compare():
    with open("test_html/index1.html", "r") as file1:
        with open("test_html/index2.html", "r") as file2:
            same = set(file1).intersection(file2)

        same.discard("\n")

        for line in same:
            print(line)
        # with open("some_output_file.txt", "w") as file_out:
        #     for line in same:
        #         file_out.write(line)


compare()
