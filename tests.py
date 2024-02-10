# Testeamos el sistema con algunos casos de prueba
import datetime

from entities import Client
from entities import AirLine
from entities import Package

import unittest


class TestAirLineTransport(unittest.TestCase):
    def setUp(self):
        self.air_line = AirLine()
        self.client_1 = Client("Cliente 1")
        self.client_2 = Client("Cliente 2")

    def test_transport_package_for_client(self):
        package = Package(self.client_1, datetime.date.today())

        result = self.air_line.transport_package(package)

        assert result == "Package for client Cliente 1 transported successfully."
        assert len(self.air_line.transported_packages) == 1
        assert self.air_line.transported_packages[0] == package

    def test_transport_multiple_packages_different_clients(self):
        package_1 = Package(self.client_1, datetime.date.today())
        package_2 = Package(self.client_2, datetime.date.today())

        result1 = self.air_line.transport_package(package_1)
        result2 = self.air_line.transport_package(package_2)

        assert result1 == "Package for client Cliente 1 transported successfully."
        assert result2 == "Package for client Cliente 2 transported successfully."
        assert len(self.air_line.transported_packages) == 2
        assert self.air_line.transported_packages[0] == package_1
        assert self.air_line.transported_packages[1] == package_2


class TestAirLineReport(unittest.TestCase):
    def setUp(self):
        self.air_line = AirLine()

        client_1 = Client("Cliente 1")
        client_2 = Client("Cliente 2")

        package_1 = Package(client_1, datetime.date.today())
        package_2 = Package(client_2, datetime.date(2022, 1, 1))

        self.air_line.transport_package(package_1)
        self.air_line.transport_package(package_2)

    def test_generate_report_without_filter_date(self):
        report = self.air_line.generate_report()
        assert report == {
            "date": None,
            "transported_packages": 2,
            "total_raised": 20
        }

    def test_valid_filter_date(self):
        filter_date = datetime.date.today()
        report = self.air_line.generate_report(filter_date)

        assert report == {
            "date": filter_date,
            "transported_packages": 1,
            "total_raised": 10
        }
