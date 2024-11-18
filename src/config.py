class Config:
    """
    Configuration class for the Polynomial Arithmetic Calculator API.

    This class contains nested classes for different configuration settings.

    Attributes:
        APP (Config.APP): Configuration settings for the application.
        Testing (Config.Testing): Configuration settings for testing.
    """

    class APP:
        """
        Configuration settings for the application.

        Attributes:
            TITLE (str): The title of the application.
            DESCRIPTION (str): A brief description of the application.
            VERSION (str): The version of the application.
        """

        TITLE = "Polynomial Arithmetic Calculator"
        DESCRIPTION = "A simple polynomial arithmetic calculator API"
        VERSION = "0.1.0"

    class Testing:
        """
        Configuration settings for testing.

        Attributes:
            RANDOM (Config.Testing.RANDOM): Random seed settings for testing.
        """

        class RANDOM:
            """
            Random seed settings for testing.

            Attributes:
                SEED (int): The seed value for random number generation.
            """

            SEED = 0
