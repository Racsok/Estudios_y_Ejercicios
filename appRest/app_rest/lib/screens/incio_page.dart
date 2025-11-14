import 'package:app_rest/API/API.dart';
import 'package:flutter/material.dart';

import '../models/Pokemon.dart';

class Inicio extends StatefulWidget {
  const Inicio({Key? key}) : super(key: key);

  @override
  _InicioState createState() => _InicioState();
}

class _InicioState extends State<Inicio> {
  late Future<List<Pokemon>> pokemon;

  @override
  void initState() {
    // TODO: implement initState
    super.initState();

    pokemon = API().getAPI();

  }
    
 
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: FutureBuilder(
          future: pokemon,
          builder: ((context, snapshot) {

            if (snapshot.hasData) {

              return GridView.builder(
                gridDelegate: const SliverGridDelegateWithFixedCrossAxisCount(
                  crossAxisCount: 4,  
                  childAspectRatio: 1.5,
                  mainAxisSpacing: 10,
                  
                ),

                itemCount: snapshot.data!.length,
                itemBuilder: (context, index) {
                 // print(snapshot.data[0]);
                  return card(
                    snapshot.data![index].id,
                    snapshot.data![index].nombre, 
                    snapshot.data![index].front_default);
                },
              );
            } else if (snapshot.hasError) {
              return Center(child: Text('Error'));
            }
            return const Center(
              child: CircularProgressIndicator(),
            );
          })),
    );
  }
  
  Widget card(int id,String nombre,String img) {
    return TextButton(onPressed: (){
      Navigator.of(context).pushNamed('/info_pokemon', arguments: id);
    },
    child: Container(
      height: 200,
      width: 150,
      
      child: Card( 
        color: Colors.blueAccent[100],
        elevation: 10,
        
        child: Padding(
          padding: const EdgeInsets.all(5),
         
          child:  Column(
            mainAxisAlignment: MainAxisAlignment.center,
            children: [
            Container(
            padding: EdgeInsets.all(10), 
            width: 55,
            height: 55,
            decoration: BoxDecoration(borderRadius: BorderRadius.circular(25), color: Colors.greenAccent[100]),
            child: Image(image: NetworkImage(img)),
            ),
            Container(padding: EdgeInsets.all(5), child: Text(nombre, style: TextStyle( color: Colors.white, fontSize: 16),)),
            Row(
              mainAxisAlignment: MainAxisAlignment.center,
              children: [
                Text('Favoritos'),
                IconButton(onPressed: (){
                  setState(() {
                    Icon(Icons.favorite);
                  });
                }, 
                icon: Icon(Icons.favorite_border), 
                color: Colors.pink,)
              ],
            ),
          ],
          )
        ),
      ),
    ));
  }
}
