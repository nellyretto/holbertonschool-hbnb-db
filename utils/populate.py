""" Populate the database with some data at the start of the application"""

from src.persistence.repository import Repository


def populate_db(repo: Repository) -> None:
    """Populates the db with a dummy country"""
    from src.models.country import Country

    countries = [
        Country(name="Uruguay", code="UY"),
        Country(name="Norway", code="NO"),
        Country(name="Korea", code="KR"),
        Country(name="Puerto Rico", code="PR"),
        Country(name="Argentina", code="AR"),
        Country(name="Mexico", code="MX"),
        Country(name="Cuba", code="CU"),

    ]

    for country in countries:
        existing_countries = repo.get_by_code(Country, country.code)
        if existing_countries is None:
            repo.save(country)

    print("Memory DB populated")
