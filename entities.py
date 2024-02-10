class Client:
    def __init__(self, name):
        self.name = name


class Package:
    def __init__(self, client, transported_date):
        self.client = client
        self.transported_date = transported_date


class AirLine:
    def __init__(self):
        self.transported_packages = []
        self.transport_charge = 10

    def transport_package(self, package):
        """
        This method is responsible for adding a package to the list of transported packages and returning
         a success message.
        :param package:
        :return: str
        """
        self.transported_packages.append(package)
        return f'Package for client {package.client.name} transported successfully.'

    def generate_report(self, filter_date=None):
        if filter_date:
            filtered_packages = [p for p in self.transported_packages if p.transported_date == filter_date]
        else:
            filtered_packages = self.transported_packages

        total_raised = len(filtered_packages) * self.transport_charge
        report_date = "" if not filter_date else filter_date.strftime("%Y-%m-%d")
        return {
            "date": report_date,
            "transported_packages": len(filtered_packages),
            "total_raised": total_raised
        }
