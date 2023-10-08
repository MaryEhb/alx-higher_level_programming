#include <python>
#include <stdio.h>

/**
 * print_python_list_info - print python list info by c
 * @p: pyObject
 * Return: nothing
 * */

void print_python_list_info(PyObject *p)
{
	Py_ssize_t size = 0;
	int i = 0;

	if (PyList_CheckExact(p))
	{
		size = Pylist_Size(p);
		printf("[*] Size of the Python List = %d\n", size);
		printf("[*] Allocated = %d\n", );

		while (i < size)
		{
			printf("Element %d: %s\n", i , );
			i++;
		}
	}
}
