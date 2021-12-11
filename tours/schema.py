import graphene
from graphene_django import DjangoObjectType

from tours.models import User, Zone, Tour, Salida


class UserType(DjangoObjectType):
    class Meta:
        model = User


class ZoneType(DjangoObjectType):
    class Meta:
        model = Zone


class TourType(DjangoObjectType):
    """ Tipo de dato para manejar el tipo Tour """

    class Meta:
        # Se relaciona con el origen de la data en models.Tour
        model = Tour


class SalidaType(DjangoObjectType):
    """ Tipo de dato para manejar el tipo Salida """

    class Meta:
        # Se relaciona con el origen de la data en models.Salida
        model = Salida


class Query(graphene.ObjectType):
    """ Definición de las respuestas a las consultas posibles """

    # Se definen los posibles campos en las consultas
    all_users = graphene.List(UserType)  # allUsers
    all_zones = graphene.List(ZoneType)  # allZonas
    all_tours = graphene.List(TourType)  # allZonas
    all_salidas = graphene.List(SalidaType)  # allZonas

    # Se define las respuestas para cada campo definido
    def resolve_all_users(self, info, **kwargs):
        # Responde con la lista de todos registros
        return User.objects.all()

    def resolve_all_zones(self, info, **kwargs):
        # Responde con la lista de todos registros
        return Zone.objects.all()

    def resolve_all_tours(self, info, **kwargs):
        # Responde con la lista de todos registros
        return Tour.objects.all()

    def resolve_all_salidas(self, info, **kwargs):
        # Responde con la lista de todos registros
        return Salida.objects.all()


class CreateZone(graphene.Mutation):
    """ Permite realizar la operación de crear en la tabla Zona """

    class Arguments:
        """ Define los argumentos para crear una Zona """
        name = graphene.String(required=True)
        description = graphene.String()
        latitud = graphene.Decimal()
        longitud = graphene.Decimal()

    # El atributo usado para la respuesta de la mutación
    zone = graphene.Field(ZoneType)

    def mutate(self, info, name, description=None, latitud=None,
               longitud=None):
        """
        Se encarga de crear la nueva Zona donde sólo nombre es obligatorio, el
        resto de los atributos son opcionales.
        """
        zone = Zone(
            name=name,
            description=description,
            latitud=latitud,
            longitud=longitud
        )
        zone.save()

        # Se regresa una instancia de esta mutación y como parámetro la Zona
        # creada.
        return CreateZone(zone=zone)


class DeleteZone(graphene.Mutation):
    """ Permite realizar la operación de eliminar en la tabla Zona """

    class Arguments:
        """ Define los argumentos para eliminar una Zona """
        id = graphene.ID(required=True)

    # El atributo usado para la respuesta de la mutación, en este caso sólo se
    # indicará con la variuable ok true en caso de éxito o false en caso
    # contrario
    ok = graphene.Boolean()

    def mutate(self, info, id):
        """
        Se encarga de eliminar la nueva Zona donde sólo es necesario el atributo
        id y además obligatorio.
        """
        try:
            # Si la zona existe se elimina sin más
            zone = Zone.objects.get(pk=id)
            zone.delete()
            ok = True
        except Zone.DoesNotExist:
            # Si la zona no existe, se procesa la excepción
            ok = False
        # Se regresa una instancia de esta mutación
        return DeleteZone(ok=ok)


class UpdateZone(graphene.Mutation):
    """ Permite realizar la operación de modificar en la tabla Zona """

    class Arguments:
        """ Define los argumentos para modificar una Zona """
        id = graphene.ID(required=True)
        name = graphene.String()
        description = graphene.String()
        longitud = graphene.Float()
        latitud = graphene.Float()

    # El campo regresado como respuesta de la mutación, en este caso se regresa
    # la zona modificada.
    zone = graphene.Field(ZoneType)

    def mutate(self, info, id, name=None, description=None, longitud=None,
               latitud=None):
        """
        Se encarga de modificar la Zona identificada por el id.
        """
        try:
            # Si la zona existe se modifica
            zone = Zone.objects.get(pk=id)
            # Si algunos de los atributos es proporcionado, entonces se
            # actualiza
            if name is not None:
                zone.name = name
            if description is not None:
                zone.description = description
            if latitud is not None:
                zone.latitud = latitud
            if longitud is not None:
                zone.longitud = longitud
            zone.save()
        except Zone.DoesNotExist:
            # Si la zona no existe, se procesa la excepción
            zona = None
        # Se regresa una instancia de esta mutación
        return UpdateZone(zone=zone)


class Mutation(graphene.ObjectType):
    create_zone = CreateZone.Field()
    delete_zone = DeleteZone.Field()
    update_zone = UpdateZone.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)
