import my_exceptions


try:
    def student_notes(filename) -> dict[str:int]:
        """Working whit file and input data"""
        # For Empty filename an Exception
        if not filename:
            raise my_exceptions.NoEncontrado(filename)
        else:
            # Openning and reading the file
            def open_read_file():
                try:
                    with open("./" + filename + ".txt", "r") as f:
                        st = f.readlines()
                    return st
                except (FileNotFoundError, IOError):
                    raise my_exceptions.NoEncontrado(filename)

            # Reordering students data from the file
            def reorder_data(st=open_read_file()):
                lines = [char.replace("\t", " ").strip("\n").split() for char in st]

                try:
                    if len(lines[0]) == 3:
                        # Names
                        keys = [
                            char[0] + " " + char[1]
                            if char[0].isalpha() and char[1].isalpha()
                            else None  # This is for handling errors if names contains numbers
                            for char in lines
                        ]
                        # Notes
                        values = [float(number[2]) for number in lines]

                        return (keys, values)
                    else:
                        # If List not contains [FirstName, SecondName, Note]
                        raise my_exceptions.LineaErronea(filename)
                # If list is empty (not index)
                except IndexError:
                    raise my_exceptions.ArchivoVacio(filename)
                # if notes values contains characters
                except (ValueError, TypeError):
                    raise my_exceptions.LineaErronea(filename)

            # Reordered data to list and Summing student notes
            def results(keys, values):
                try:
                    alumns = dict()
                    for name, notes in zip(keys, values):

                        if name not in alumns:
                            alumns[name] = notes
                        else:
                            alumns[name] += notes

                    sorted_alumns = dict(sorted(alumns.items()))  # Reorder list
                    return sorted_alumns

                except TypeError:
                    # For any TypeError
                    raise my_exceptions.LineaErronea(filename)

            # Results
            return results(*reorder_data())


    def show_results(filename):
        """Showing results for student notes"""
        final_notes = student_notes(filename)
        if final_notes == {}:
            # Empty File
            raise my_exceptions.ArchivoVacio(filename)
        else:
            print("\nstudent notes".upper())
            print("=" * 16)
            for key, value in final_notes.items():
                print(key, value)
            print("=" * 16 + "\n")
except Exception:
    raise my_exceptions.ExcepcionDatosAlumnos(filename=None) 