#include "iostream"

int	main()
{
	std::time_t	now = std::time(0);
	std::tm		*local = std::localtime( & now );

	// 1st way to print time
	std::cout << std::asctime(local);

	char	buffer[32];

	// 2nd way to print time
	std::strftime(buffer, 32, "%a, %d.%m.%Y %H:%M:%S", local);
	std::cout << buffer << std::endl;
}
