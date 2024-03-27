from django.contrib.auth.models import User

def create_user(new_user):
  try:
    user = User.objects.create_user(
      new_user["name"],
      new_user["email"],
      new_user["password"]
    )
    user.save()
    return { "error": False, "msg": "Usuario creado exitosamente" }
  except Exception as err:
    print(err)
    return { "error": True, "msg": "El usuario ya existe" }