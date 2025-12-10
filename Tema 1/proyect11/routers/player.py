from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

#Creamos una apicacion FastAPI  
router = APIRouter(prefix="/players", tags=["players"])

#Creamos la clase Jugador
class Player(BaseModel):
    id: int #Id del jugador
    name: str #Nombre del jugador
    age: int #Edad del jugador
    position: str #Posicion del jugador
    nationality: str #Nacionalidad del jugador
    salary: float #Salario del jugador
    id_team: int #Id del equipo al que pertenece el jugador

#Lista de jugadores de ejemplo
player_list = [
    Player(id=1, name="Isco", age=31, position="Midfielder", nationality="Spanish", salary=350000, id_team=1),
    Player(id=2, name="Robert Lewandowski", age=35, position="Forward", nationality="Polish", salary=800000, id_team=2),
    Player(id=3, name="Jude Bellingham", age=20, position="Midfielder", nationality="English", salary=750000, id_team=3),
    Player(id=4, name="Antoine Griezmann", age=32, position="Forward", nationality="French", salary=600000, id_team=4),
    Player(id=5, name="Sergio Ramos", age=37, position="Defender", nationality="Spanish", salary=450000, id_team=5),
    Player(id=6, name="José Gayà", age=28, position="Defender", nationality="Spanish", salary=300000, id_team=6),
    Player(id=7, name="Gerard Moreno", age=31, position="Forward", nationality="Spanish", salary=350000, id_team=7),
    Player(id=8, name="Iñaki Williams", age=29, position="Forward", nationality="Ghanaian", salary=300000, id_team=8),
    Player(id=9, name="Take Kubo", age=22, position="Forward", nationality="Japanese", salary=250000, id_team=9),
    Player(id=10, name="Iago Aspas", age=36, position="Forward", nationality="Spanish", salary=400000, id_team=10)
]


#Funcion para obtener el siguiente ID disponible
def next_id():
    return max(player_list, key = id).id + 1


def search_player(id: int):
    #players = filter(lambda player: player.id==id, player_list)
    return [player for player in player_list if player.id == id]


#region Metodos get
#Metodo get para obtener todos los jugadores
@router.get("/")
def get_players():
    return player_list


#Metodo get para obtener el jugador por su id
@router.get("/{id_player}")
def get_player_by_id(id_player: int):

    #Buscamos el jugador por su ID y lo almacenamos en una lista
    players = search_player(id_player)

    #Si encontramos al jugadorlo devolvemos
    if len(players) != 0:
        return players[0]

    #Si no encontramos al jugador devolvemos un mensaje de error
    else:
        raise HTTPException(status_code=404, detail="Player not found")
#endregion


#region Metodos post
#Metodo post para añadir un nuevo jugador
@router.post("/", status_code=201)
def add_player(player: Player):

    #LLamamos a la funcion para asignar un ID al nuevo jugador 
    player.id = next_id()

    #Añadimos el nuevo jugador a la lista de jugadores
    player_list.routerend(player)

    #Devolvemos el jugador que se ha añadido
    return player
#endregion


#region Metodos put
#Metodo put para modificar un jugador existente
@router.put("/{id_player}", response_model = Player)
def modify_player(id_player: int, player: Player):

    #Creamos un bucle for para recorrer la lista de jugadores
    for index, saved_player in enumerate(player_list):

        #Si el id del jugador es igual al id que queremos modificar, modificamos el jugador
        if saved_player.id == id_player:

            #Asignamos el ID al jugador modificado
            player.id = id_player

            #Actualizamos el jugador en la lista de jugadores
            player_list[index] = player

            #Devolvemos el jugador que se ha modificado
            return player

    #Si no encontramos al jugador devolvemos un mensaje de error
    raise HTTPException(status_code = 404, detail = "Player not found")
#endregion


#region Metodos delete
#Metodo delete para eliminar un jugador existente
@router.delete("/{id_player}")
def delete_player(id_player: int):

    #Creamos un bucle for para recorrer la lista de jugadores
    for saved_player in player_list:

        #Si el id del jugador es igual al id que queremos eliminar, eliminamos el jugador
        if saved_player.id == id_player:

            #Eliminamos el jugador de la lista de jugadores
            player_list.remove(saved_player)

            #Devolvemos un diccionario vacio
            return {}
    
    #Si no encontramos al jugador devolvemos un mensaje de error
    raise HTTPException(status_code = 404, detail = "Player not found")
#endregion