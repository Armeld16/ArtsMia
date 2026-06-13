from dataclasses import dataclass

@dataclass
class ArtObject:
    object_id: int
    classification: str
    continent: str
    country: str
    curator_approved: int
    dated: str
    department: str
    medium: str
    nationality: str
    object_name: str
    restricted: int
    rights_type: str
    role: str
    room: str
    style: str
    title: str
    # una volta copiati tutti e messi o interi o stringe, mi servono i metodi
    # hash molto fondamentale ed è hash della object_id (chiava primaria )
    # confrontabili eq , sono uguali se hanno la stessa chiave primaria
    # return str , che è il metodo che utilizzeremo per stampare oggetto
    def __hash__(self):
        return hash(self.object_id)
    def __eq__(self, other):
        return self.object_id == other.object_id

    def __str__(self):
        return f"{self.title} ({self.dated}) -- {self.classification}"
