import 'package:flutter/material.dart';

void main() {
  runApp(const AfricaAIApp());
}

class AfricaAIApp extends StatelessWidget {
  const AfricaAIApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Africa AI',
      theme: ThemeData(primarySwatch: Colors.blue),
      home: const HomeScreen(),
    );
  }
}

class HomeScreen extends StatelessWidget {
  const HomeScreen({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: const Text('Africa AI App')),
      body: const Center(child: Text('Hello from Africa AI!')),
    );
  }
}
