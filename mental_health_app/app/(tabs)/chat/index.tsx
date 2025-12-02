import { ScrollView, Text, View, StyleSheet, Button } from "react-native";
import { useRouter } from "expo-router";

export default function Chats() {

    const router = useRouter();

    const id = 123;

    return (
        <View style={{flex: 1}}>
            <ScrollView style={{ flex: 1, backgroundColor: 'white' }}>
                <View style={{ padding: 20 }}>
                    <Text style={{ color: 'black', fontSize: 24, textAlign: "center" }}>Chats</Text>
                </View>
            </ScrollView>

        <Button 
        title="Go to Chat" 
        onPress={() => router.push(`/chat/${id}`)}/>
      </View>
    );
}