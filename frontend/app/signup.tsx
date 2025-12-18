import { ScrollView, View, Text, StyleSheet } from "react-native";

export default function Signup() {
    return(
        <ScrollView style={{ flex: 1, backgroundColor: 'white' }}>
            <View style={{ padding: 20 }}>
                <Text style={{ color: 'black', fontSize: 24, textAlign: "center" }}>Signup</Text>
            </View>
        </ScrollView>
    );
}