#include <Python.h>
#include <stdlib.h>

/**
 * print_python_list_info - prints information about a python list object
 * @p: pointer to generic pyobject which is a pyListobject type
 *
 * Return: always void
 */
void print_python_list_info(pyobject *p)
{
	pyListobject *py_list = NULL;
	ssize_t list_len = 0;
	ssize_t i = 0;
	const char *ele_type = NULL;

	list_len = pyList_Size(p);
	py_list = (pyListobject *)p;
	printf("[*] size of the pyhton List = %ld\n", list_len);
	printf("[*] Allocated = %ld\n", (signed long)(py_list->allocated));
	while (i < list_len)
	{
		ele_type = py_TYPE(pt_list->ob_item[i]->tp_name;
		printf("Element %ld: %s\n", i, ele_type);
		i++;
	}
}
