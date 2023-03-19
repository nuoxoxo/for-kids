#include "iostream"

int	main()
{
	// get time_t
	std::time_t	now = std::time(0);
	std::tm		*local = std::localtime( & now );


	// 1st way to print time
	std::cout << std::asctime(local);


	// 2nd way to print time
	char	buffer[32];
	std::strftime(buffer, 32, "%a, %d.%m.%Y %H:%M:%S", local);
	std::cout << buffer << std::endl;
}
