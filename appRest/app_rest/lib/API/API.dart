import 'dart:convert';
import 'package:flutter/material.dart';
import 'package:http/http.dart' as http;
import '../models/Pokemon.dart';

class API{
    String urlAPI = "https://pokeapi.co/api/v2/pokemon/";

    Future<List<Pokemon>>getAPI() async{
      var client = http.Client();
      var url = Uri.parse(urlAPI);
      var response = await http.get(url);

      List<Pokemon> pokemonAPI = [];

      if (response.statusCode == 200) {
        final jsonData = jsonDecode(response.body);
        for (var item in jsonData['results']) {
          var json = Uri.parse(item['url']);
          var info = await http.get(json);
          final jsonUrl = jsonDecode(info.body);
          pokemonAPI.add(Pokemon(
            jsonUrl['id'],
            item['name'], 
            jsonUrl['sprites']['other']['home']['front_default']));
        }

        return pokemonAPI;
      }else{
        throw Exception('hubo un error');
      }

    }
}