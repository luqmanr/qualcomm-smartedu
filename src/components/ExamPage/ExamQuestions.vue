<template>
    <div style="height:100%;">
        <div style="font-weight: bolder; font-size: larger; margin-bottom: 2vh;">PERTANYAAN UJIAN</div>
        <div v-for="question,index in questionAnswers" class="row" style="margin-bottom: 2vh;">
            <span class="col-sm-12" style="margin-bottom: 2vh;">{{index+1}}. {{question.question}}</span>
            <!-- <input v-for="answers in question.answers" :name="question.question" type="radio" :value="answers">{{answers}}</input> -->
            <div v-for="answers,ansIndex in question.answers" class="col-sm-12">
                
                <label>
                    <input type="radio" :id="answers" :name="index" @click="updateAnswer(index, ansIndex)">
                    <span style="margin-left: 2vw;">{{answers}}</span>
                </label>

            </div>
        </div>

        <!-- <button @click="emitAnswers">SUBMIT ANSWERS</button> -->

    </div>
</template>

<script>

import examQuestionsJSON from './exam_questions.json'

export default {
    data() {
        return {
            examQuestions: examQuestionsJSON,
            userAnswers: []
        }
    },
    computed: {
        questionAnswers() {
            return examQuestionsJSON.data.map(questions => {
                return questions
            })
        }
    },
    methods: {
        getQuestionsLength() {
            var index = examQuestionsJSON.data.length
            var i
            for (i in examQuestionsJSON.data) {
                // console.log(i)
                this.userAnswers.push(null)
            }
            // console.log(this.userAnswers)
        },
        updateAnswer(index, answers) {
            this.userAnswers[index] = answers;
            console.log(this.userAnswers)
        },
        emitAnswers() {
            this.$emit("emitAnswers", this.userAnswers)
        }
    },
    created() {
        this.getQuestionsLength()
    },
    watch: {
        userAnswers() {
            this.emitAnswers()
        }
    }
}
</script>

<style scoped>

</style>