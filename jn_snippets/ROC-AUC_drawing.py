probabilities_valid = best_rfc_est.predict_proba(x_test)
probabilities_one_valid = probabilities_valid[:, 1]
auc_roc = roc_auc_score(y_test,probabilities_one_valid)
print("AUC-ROC = ", round(auc_roc, 2))

fig, ax = plt.subplots(figsize=(14,8))
fpr, tpr, thresholds = roc_curve(y_test, probabilities_one_valid)
plt.plot([0, 1], [0, 1], linestyle='--')
plt.plot(fpr, tpr)
plt.xlim([0.0, 1.0])
plt.ylim([0.0, 1.0])
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title('ROC-кривая')
plt.show()