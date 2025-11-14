import 'package:app_rest/screens/incio_page.dart';
import 'package:flutter/material.dart';

import 'package:app_rest/screens/info_pokemon.dart';

class MainApp extends StatelessWidget {
  const MainApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      debugShowCheckedModeBanner: false,
      title: 'AppiRest',
      initialRoute: '/',
      routes: {
        '/': (BuildContext context) => Inicio(),
        '/info_pokemon': (BuildContext context) => InfoPage(),
      },
    );
  }
}
