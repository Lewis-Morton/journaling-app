import { ScrollView, Text, View, StyleSheet, Button} from "react-native";
import { useRouter } from "expo-router";

export default function HomeScreen() {

  const router = useRouter(); 

  const id = 123; // just to test

  return (
    <View style={{flex: 1}}>
      <ScrollView style={{ flex: 1, backgroundColor: 'white' }}>
        <View style={{ padding: 20 }}>
          <Text style={{ color: 'black', fontSize: 24, textAlign: "center" }}>Home Screen
          </Text>
        </View>
      </ScrollView>
            
      
      <Button 
      title="Go to Journal" 
      onPress={() => router.push(`/journal/${id}`)}/>
    </View>
  );
}
      
    



