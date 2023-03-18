#include "iostream"

int	main()
{
	std::time_t	result = std::time(0);

	std::cout << std::asctime(std::localtime(&result));




}
