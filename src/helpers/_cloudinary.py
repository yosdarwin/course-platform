import cloudinary
from decouple import config

# Configuration
CLOUDINARY_CLOUD_NAME = config("CLOUDINARY_NAME", default="")
CLOUDINARY_PUBLIC_API_KEY = config(
    "CLOUDINARY_PUBLIC_API_KEY", default="788443666991344")
CLOUDINARY_SECRET_API_KEY = config("CLOUDINARY_SECRET_API_KEY", default="")
cloudinary.config(
    cloud_name=CLOUDINARY_CLOUD_NAME,
    api_key="788443666991344",
    # Click 'View API Keys' above to copy your API secret
    api_secret="<your_api_secret>",
    secure=True
)
