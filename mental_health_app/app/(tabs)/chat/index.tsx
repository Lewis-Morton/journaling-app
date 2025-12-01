import { ScrollView, Text, View, StyleSheet } from "react-native";

export default function Chats() {
    return (
        <ScrollView style={{ flex: 1, backgroundColor: 'white' }}>
            <View style={{ padding: 20 }}>
                <Text style={{ color: 'black', fontSize: 24, textAlign: "center" }}>Chats</Text>
            </View>
        </ScrollView>
    );
}