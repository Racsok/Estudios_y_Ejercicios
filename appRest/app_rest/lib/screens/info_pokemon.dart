import 'package:app_rest/API/API.dart';
import 'package:flutter/material.dart';

import '../models/Pokemon.dart';

class InfoPage extends StatefulWidget {
  const InfoPage({Key? key}) : super(key: key);

  @override
  State<InfoPage> createState() => _InfoState();
}

class _InfoState extends State<InfoPage> {
 late Future<List<Pokemon>> pokemon;


  @override
  void initState() {
    // TODO: implement initState
    super.initState();
    pokemon = API().getAPI();
  }

  @override
  Widget build(BuildContext context) {
    final name = ModalRoute.of(context)?.settings.arguments;
    var num = name.toString();
    return Scaffold(
        appBar: AppBar(
          title: Text('hola'),
        ),
        body: FutureBuilder(
          future: pokemon,
          builder: ((context, snapshot) {

            if (snapshot.hasData) {
              return Text(snapshot.data![int.parse(num)-1].nombre);
            }
            return Center(
              child: CircularProgressIndicator(),
            );
          }),
        ));
  }
}
