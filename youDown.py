#Esta en una app sencilla, echale un ojo
#Se que me falta mucho por mejorar
#Agradezco cualquier consejo


#Importacion de las librerias
from pytube import YouTube
import flet
from flet import (
        BottomSheet,
        Container,
        ElevatedButton,
        Image,
        MainAxisAlignment,
        Page,
        Row,
        Text,
        TextAlign,
        TextField,
        ThemeMode
        )


#Ventana principal.
#Intente que fuese la ventana estuviera en un solor archivo
#pero simplemente no lo logre.
#Estoy empezando con python @un mes y medio aprox
def ventana(page: Page):
    page.theme_mode = ThemeMode.DARK
    page.bgcolor = '#1E293B'
    page.window_width = 300
    page.window_height = 550
    page.vertical_alignment = MainAxisAlignment.CENTER
    
    #Defino las funciones
    #intente que las @clases estuvieran primero,
    #pero me daba error.
    def abrir_alerta(e):
        Estilos.alerta.open = True
        Estilos.alerta.update()

    def down_mp3(e):
        link_mp3 = YouTube(str(url.value))
        yt = link_mp3.streams.get_audio_only()
        yt.download()
        abrir_alerta(e)
        url.value = ''
        page.update()

    def down_mp4(e):
        link_mp4 = YouTube(str(url.value))
        yt = link_mp4.streams.get_highest_resolution()
        yt.download()
        abrir_alerta(e)
        url.value = ''
        page.update()
    

    #Aqui estan un tipo de @clases
    #debo mejorar, lo se

    class Titulo:
        titulo = Container(
                width=250,
                height=80,
                bgcolor='#334155',
                border_radius= 10,
                content= 
                Row([
                    Text(
                        value='youDown',
                        size=35,
                        ),
                    Image(
                        src='./icon.png',
                        height=50,
                        width=45,
                        )
                    ], alignment=MainAxisAlignment.CENTER)
                )

    class Estilos:
        btn_mp3 = ElevatedButton(
                color='#ffffff',
                bgcolor='red',
                text='mp3',
                on_click= down_mp3
                )
        btn_mp4 = ElevatedButton(
                color='#ffffff',
                bgcolor='green',
                text='mp4',
                on_click=down_mp4
                )
        url = TextField(
                bgcolor='#334155',
                opacity=0.3,
                border_width=0,
                border_radius=10,
                )
        alerta = BottomSheet(
                content=Container(
                    bgcolor='#0D1826',
                    height=150,
                    border_radius=10,
                    content=(
                        Row([
                            Text(
                                value='''Se ha descargado 
con exito!!''',
                                text_align=TextAlign.START, 
                                size=25
                                )
                            ])
                        )
                    )
                )
        

    #esto se ve feo, pero fue la forma
    #en que funciono
    btn_mp3 = Estilos.btn_mp3
    btn_mp4 = Estilos.btn_mp4
    url = Estilos.url
    titulo = Titulo.titulo
    
    #aqui se agregan los elementos a la pantalla
    page.add(
            Row([
                titulo,
                ], alignment=MainAxisAlignment.CENTER),
            url,
            Row([
                btn_mp3,
                btn_mp4,
                ], alignment=MainAxisAlignment.CENTER),
            Estilos.alerta
            )

if __name__ == "__main__":
    flet.app(target=ventana)
